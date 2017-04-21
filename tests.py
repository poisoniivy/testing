"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn("having a party", str(result.data))

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        result = self.client.get("/")
        self.assertIn("<h2>Please RSVP</h2>", str(result.data))
        # FIXME: Add a test to show we haven't RSVP'd yet
        print "No RSVP test works."

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)
        self.assertIn("<h2>Party Details</h2>", str(result.data))
        
        self.assertNotIn('<input type="submit" value="Oooh! I want to come!" class="btn btn-primary">', 
                        str(result.data))
        # FIXME: check that once we log in we see party details--but not the form!
        
        print "RSVP Test works"

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        rsvp_info = {'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)


        # result = self.client.get("/")
        # self.assertTrue(party.is_mel("Mel Melitpolski", "some email"))
        # self.assertTrue(party.is_mel("Mel Melitpolski", "mel@ubermelon.com"))
        # self.assertTrue(party.is_mel("Melonhead", "mel@ubermelon.com"))
        # self.assertFalse(party.is_mel("Caroline", "caro@line.com"))
        self.assertIn("Sorry, Mel. This is kind of awkward.", str(result.data))
        print "No Mel test works"


if __name__ == "__main__":
    unittest.main()
