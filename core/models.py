from dataclasses import dataclass, field

DEFAULT_STATUSES = ["listened", "want-to-listen", 'favorite', None]
@dataclass
class Album:
    artist: str
    title: str
    release_year: str
    status: str = "want-to-listen"
    tags : list[str] = field(default_factory=list)
    source: str | None = None # e.g. "manual" "last-fm"
    mbid: str | None = None # musicbrainz ID
