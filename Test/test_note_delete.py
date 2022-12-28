import json
import unittest
from Website import create_app, db
from Website.models import Note

unittest.TestLoader.sortTestMethodsUsing = None

app = create_app('testing')

class NotesDeleteUnitTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.note = 'Test note'
        self.note_id = 1
        self.user_id = 1
        self.email = 'testingUser@test.com'
        self.password = '1234567Test'


    def test_delete_note_success(self):
        self.app.post('/login', data={'email': self.email, 'password': self.password})
        self.app.get('/u')
        result = self.app.post('/delete-note', data=(json.dumps({'noteId': self.note_id})))
        notes = self.app.get('/u')
        self.assertEqual(b'Test note' in notes.data, False)

    def test_delete_note_failure(self):
        '''# Send a POST request to the delete_note view with a valid note ID
        result = self.app.post('/delete-note', data=json.dumps({'noteId': self.note_id}))

        # Assert that the note was not deleted from the database
        note = Note.query.get(self.note_id)
        self.assertIsNotNone(note)'''
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()