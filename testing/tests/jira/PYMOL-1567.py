"""
PYMOL-317
can't select by atom type
"""

import os
from pymol import cmd, testing, stored


@testing.requires("incentive")
@testing.requires("no_edu")
class TestPYMOL1567(testing.PyMOLTestCase):

    def testAtomStateLevelSettingsOnRemove(self):
        if cmd.get_setting_int("suspend_undo"):
            self.skipTest("need suspend_undo=0")

        cmd.load(self.datafile("1molecule.mae"))
        cmd.load(self.datafile("1molecule.mae"))
        cmd.label("index 10", "'Test Label'")
        plv = [5.0, 0.0, 0.0]
        cmd.alter_state(1, "index 10", "s.label_placement_offset = %s" % plv)
        cmd.remove("index 10")
        cmd.undo()
        stored.offset = None
        cmd.iterate_state(
            1, "index 10", "stored.offset = list(s.label_placement_offset)"
        )
        self.assertEqual(stored.offset, plv)

    def testAtomLevelSettingsOnRemove(self):
        if cmd.get_setting_int("suspend_undo"):
            self.skipTest("need suspend_undo=0")

        cmd.load(self.datafile("1molecule.mae"))
        cmd.load(self.datafile("1molecule.mae"))
        cmd.label("index 10", "'Test Label'")
        plv = [5.0, 0.0, 0.0]
        cmd.alter("index 10", "s.label_placement_offset = %s" % plv)
        cmd.remove("index 10")
        cmd.undo()
        stored.offset = None
        cmd.iterate_state(
            1, "index 10", "stored.offset = list(s.label_placement_offset)"
        )
        self.assertEqual(stored.offset, plv)

    def testAtomLevelSettingsOnRemove2(self):
        if cmd.get_setting_int("suspend_undo"):
            self.skipTest("need suspend_undo=0")

        cmd.load(self.datafile("1molecule.mae"))
        cmd.load(self.datafile("1molecule.mae"))
        cmd.label("index 10", "'Test Label'")
        plv = [5.0, 0.0, 0.0]
        cmd.alter("index 10", "s.label_placement_offset = %s" % plv)
        cmd.remove("index 10")
        cmd.undo()
        stored.offset = None
        cmd.iterate("index 10", "stored.offset = list(s.label_placement_offset)")
        self.assertEqual(stored.offset, plv)
