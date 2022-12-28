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

    def test_delete_note_failure(self):
        self.app.post('/login', data={'email': self.email, 'password': self.password})
        notes = self.app.get('/u')
        self.assertEqual(b'Test note' in notes.data, True)
        result = self.app.post('/delete-note', data=json.dumps({'noteId': 4}))
        notes = self.app.get('/u')
        self.assertEqual(b'Test note' in notes.data, True)

    def test_delete_note_success(self):
        self.app.post('/login', data={'email': self.email, 'password': self.password})
        notes = self.app.get('/u')
        self.assertEqual(b'Test note' in notes.data, True)
        result = self.app.post('/delete-note', data=(json.dumps({'noteId': self.note_id})))
        notes = self.app.get('/u')
        self.assertEqual(b'Test note' in notes.data, False)



if __name__ == '__main__':
    unittest.main()