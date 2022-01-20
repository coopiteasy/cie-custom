import odoo.tests.common as common
from odoo.exceptions import AccessError


class TestHRDataAcess(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self._create_users()
        self._create_employees()
        self._create_timesheets()
        self._create_test_environement()

    def _create_users(self):
        # creating users with the same groups as Marc Demo
        demo_groups = self.env.ref("base.user_demo").groups_id
        self.bigboss_uid = self.env["res.users"].create(
            {
                "name": "Bigboss",
                "login": "bigboss",
                "email": "",
                "groups_id": demo_groups,
            }
        )
        self.boss_uid = self.env["res.users"].create(
            {"name": "Boss", "login": "boss", "email": "", "groups_id": demo_groups}
        )
        self.employee_uid = self.env["res.users"].create(
            {
                "name": "Employee",
                "login": "employee",
                "email": "",
                "groups_id": demo_groups,
            }
        )
        self.external_uid = self.env["res.users"].create(
            {
                "name": "External",
                "login": "external",
                "email": "",
                "groups_id": demo_groups,
            }
        )

    def _create_employees(self):
        self.bigboss_employee_id = self.env["hr.employee"].create(
            {"name": "BigBoss", "user_id": self.bigboss_uid.id}
        )
        self.boss_employee_id = self.env["hr.employee"].create(
            {
                "name": "Boss",
                "user_id": self.boss_uid.id,
                "parent_id": self.bigboss_employee_id.id,
            }
        )
        self.employee_employee_id = self.env["hr.employee"].create(
            {
                "name": "Employee",
                "user_id": self.employee_uid.id,
                "parent_id": self.boss_employee_id.id,
            }
        )
        self.external_employee_id = self.env["hr.employee"].create(
            {"name": "External", "user_id": self.external_uid.id}
        )

    def _create_timesheets(self):
        self.bigboss_timesheet_id = self.env["hr_timesheet.sheet"].create(
            {"employee_id": self.bigboss_employee_id.id}
        )
        self.boss_timesheet_id = self.env["hr_timesheet.sheet"].create(
            {"employee_id": self.boss_employee_id.id}
        )
        self.employee_timesheet_id = self.env["hr_timesheet.sheet"].create(
            {"employee_id": self.employee_employee_id.id}
        )
        self.external_timesheet_id = self.env["hr_timesheet.sheet"].create(
            {"employee_id": self.external_employee_id.id}
        )

    def _create_test_environement(self):
        self.bigboss_test_env = self.env["hr_timesheet.sheet"].sudo(self.bigboss_uid)
        self.boss_test_env = self.env["hr_timesheet.sheet"].sudo(self.boss_uid)
        self.employee_test_env = self.env["hr_timesheet.sheet"].sudo(self.employee_uid)
        self.external_test_env = self.env["hr_timesheet.sheet"].sudo(self.external_uid)

    def test_hr_access(self):
        # External can access her own timesheet
        self.assertEqual(
            self.external_test_env.browse(self.external_timesheet_id.id).employee_id,
            self.external_employee_id,
        )

        # Employee can access her own timesheet
        self.assertEqual(
            self.employee_test_env.browse(self.employee_timesheet_id.id).employee_id,
            self.employee_employee_id,
        )

        # BigBoss can access Boss timesheet
        self.assertEqual(
            self.bigboss_test_env.browse(self.boss_timesheet_id.id).employee_id,
            self.boss_employee_id,
        )

        # BigBoss can access Employee timesheet
        self.assertEqual(
            self.bigboss_test_env.browse(self.employee_timesheet_id.id).employee_id,
            self.employee_employee_id,
        )

        # External cannot see any other timesheet
        with self.assertRaises(AccessError):
            self.external_test_env.browse(self.bigboss_timesheet_id.id).name
        with self.assertRaises(AccessError):
            self.external_test_env.browse(self.boss_timesheet_id.id).name
        with self.assertRaises(AccessError):
            self.external_test_env.browse(self.employee_timesheet_id.id).name

        # Employee cannot see her bosses timesheets
        with self.assertRaises(AccessError):
            self.employee_test_env.browse(self.bigboss_timesheet_id.id).name
        with self.assertRaises(AccessError):
            self.employee_test_env.browse(self.boss_timesheet_id.id).name

        # Boss cannot see Bigboss timesheet
        with self.assertRaises(AccessError):
            self.boss_test_env.browse(self.bigboss_timesheet_id.id).name

        # BigBoss cannot see External timesheet
        with self.assertRaises(AccessError):
            self.bigboss_test_env.browse(self.external_timesheet_id.id).name
