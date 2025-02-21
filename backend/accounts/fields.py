# filepath: accounts/fields.py
from django.db import models, connection

class SequenceField(models.CharField):
    def __init__(self, sequence_name, prefix='', *args, **kwargs):
        self.sequence_name = sequence_name
        self.prefix = prefix
        kwargs['max_length'] = kwargs.get('max_length', 20)  # Set a default max_length
        kwargs['unique'] = True
        kwargs['blank'] = True  # Allow blank values during object creation
        kwargs['editable'] = False  # Make the field non-editable in the admin
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT nextval('{self.sequence_name}')")
                value = cursor.fetchone()[0]
            return f"{self.prefix}{str(value).zfill(4)}"  # Pad with leading zeros and add prefix
        else:
            return super().pre_save(model_instance, add)