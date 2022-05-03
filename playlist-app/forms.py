"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Optional

from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    
    name = StringField(
        "Name",
        validators=[InputRequired()],
    )
    description = StringField(
        "Description",
        validators=[Optional()],
    )

class SongForm(FlaskForm):
    """Form for adding songs."""
    
    title = StringField(
        "Title",
        validators=[InputRequired()],
    )
    artist = StringField(
        "Artist",
        validators=[InputRequired()],
    )


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
