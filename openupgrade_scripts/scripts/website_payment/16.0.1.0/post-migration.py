# Copyright 2023-2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "website_payment", "16.0.1.0/noupdate_changes.xml")
    openupgrade.delete_record_translations(
        env.cr,
        "website_payment",
        [
            "mail_template_donation",
        ],
        [
            "name",
        ],
    )