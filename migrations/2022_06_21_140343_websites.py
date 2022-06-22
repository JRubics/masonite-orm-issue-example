"""Websites Migration."""

from masoniteorm.migrations import Migration


class Websites(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name', 30)
            table.timestamps()

        with self.schema.create("websites") as table:
            table.increments('id')
            table.integer('user_id').unsigned()
            table.foreign('user_id', name='websites_user_id_foreign') \
                .references('id').on('users') \
                .on_delete('cascade')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
        self.schema.drop('websites')
