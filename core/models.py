from dataclasses import dataclass, field

status_config = {
    # leave uncategorized first 
    'default_statuses' : [None, "listened", "want-to-listen"],
    'status_prompt' : "Status: [1] Listened [2] Want to Listen [0] Skip"   
}

@dataclass
class Album:
    artist: str
    title: str
    release_year: str
    # release_date: str = '0000-00-00'
    # def release_year(self) -> str: 
    #     return self.release_date.split('-')[0]
    status: str | None = status_config['default_statuses'][-1] 
    tags : list[str] = field(default_factory=list)
    source: str | None = 'user' # e.g. "user' "last-fm"
    mbid: str | None = None # musicbrainz ID
    def __str__(self):
        tags_str = ""
        if self.tags:
            tags_str = f"\nTags: {", ".join(self.tags)}"
        
        status_str = ""
        if self.status is not None: # != status_config['default_statuses'][0]
            status_str = f"[{self.status}]"
            
        release_year_str = "(N/A)"
        if self.release_year:
            release_year_str = f"({self.release_year})"

        return f"{self.artist} - {self.title} {release_year_str} {status_str} {tags_str}\nMusicBrainz ID: {self.mbid}"

# @dataclass
# class MBAlbum:
#     '''
#     Stores all MusicBrainz release-group keys
#     '''
#     artist: str
#     title: str
#     release_year: str
#     status: str | None = None
#     tags : list[str] = field(default_factory=list)
#     source: str | None = 'user' # e.g. "user' "last-fm"
#     mbid: str | None = None # musicbrainz ID
#     # def release_year(self):
#     #   return self.release_date.split('-')[0]
#     def __str__(self):
#         tags_str = ""
#         if self.tags:
#             tags_str = f"\nTags: {", ".join(self.tags)}"
#             
#         return f"{self.artist} - {self.title} ({self.release_year}) [{self.status}] {tags_str}\nMusicBrainz ID: {self.mbid}"
