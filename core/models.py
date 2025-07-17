from dataclasses import dataclass, field

# leave uncategorized last
DEFAULT_STATUSES = ["listened", "want-to-listen", "uncategorized"]

@dataclass
class Album:
    artist: str
    title: str
    release_year: str
    status: str = 'uncategorized'
    tags : list[str] = field(default_factory=list)
    source: str | None = 'user' # e.g. "user' "last-fm"
    mbid: str | None = None # musicbrainz ID
    # def release_year(self):
    #   return self.release_date.split('-')[0]
    def display(self, show_status = True, show_tags = True):
        status_string = ""
        if show_status:
            status_string = f"[{self.status}]"
        print(f"{self.artist} - {self.title} ({self.release_year}) {status_string}")
        if show_tags:
            print(f"Tags: {self.tags}")
        
