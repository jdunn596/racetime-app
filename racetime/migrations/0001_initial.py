# Generated by Django 3.0.1 on 2020-01-04 17:47

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='Used to log in, and for any important messages related to your account. We do not share your email with third parties.', max_length=255, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(db_index=True, default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('name', models.CharField(db_index=True, help_text='Who you want to be known as on the site (3-25 characters).', max_length=25, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='Name cannot contain @ or #', regex='[\\x00@#]')])),
                ('discriminator', models.CharField(db_index=True, help_text='Used to distinguish identical names.', max_length=4, validators=[django.core.validators.RegexValidator('^\\d{4}$', 'Must be 4 digits long (e.g. 1234).')])),
                ('avatar', models.ImageField(blank=True, help_text='Recommended size: 100x100. No larger than 100kb.', null=True, upload_to='')),
                ('is_staff', models.BooleanField(default=False, editable=False)),
                ('is_supporter', models.BooleanField(default=False)),
                ('twitch_code', models.CharField(max_length=30, null=True)),
                ('twitch_id', models.PositiveIntegerField(null=True)),
                ('twitch_name', models.CharField(max_length=25, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The full name of this category, e.g. "Super Mario 64".', max_length=255, unique=True)),
                ('short_name', models.CharField(help_text='An abbreviation or other short identifier, e.g. "SM64".', max_length=16, unique=True)),
                ('slug', models.CharField(help_text='A unique identifier for this category used in the URL, e.g. "tetris-99".', max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, help_text='Recommended size: 285x380. No larger than 100kb.', null=True, upload_to='')),
                ('info', models.TextField(blank=True, help_text='Displayed on the category page. Limited use of HTML is allowed.', null=True)),
                ('streaming_required', models.BooleanField(default=True, help_text='Require entrants to be streaming when they join a race. Moderators may override this for individual races.')),
                ('active', models.BooleanField(default=True, help_text='Allow new races to be created in this category.')),
                ('slug_words', models.TextField(blank=True, default=None, help_text='Set a number of words to be picked at random for race room names. If set, you must provide a minimum of 100 distinct words to use. Changing slug words will not impact existing race rooms.', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('moderators', models.ManyToManyField(blank=True, help_text='Users who can moderate races in this category.', related_name='mod_categories', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='The user who controls this category.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The win conditions for the race, e.g. "16 stars".', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Any additional information or rules that apply to this race goal.', max_length=2000, null=True)),
                ('active', models.BooleanField(default=True, help_text='Allow new races to be created with this goal.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetime.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=255)),
                ('name', models.CharField(max_length=25)),
                ('discriminator', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_goal', models.CharField(blank=True, default=None, help_text='Set a custom goal for this race, if none of the category goals are suitable. Custom races cannot be recorded.', max_length=255, null=True)),
                ('info', models.TextField(blank=True, help_text='Any useful information for race entrants.', max_length=1000, null=True)),
                ('slug', models.SlugField()),
                ('state', models.CharField(choices=[('open', 'Open'), ('invitational', 'Invitational'), ('pending', 'Getting ready'), ('in_progress', 'In progress'), ('finished', 'Finished'), ('cancelled', 'Cancelled')], default='open', max_length=50)),
                ('opened_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(null=True)),
                ('ended_at', models.DateTimeField(null=True)),
                ('recordable', models.BooleanField(default=True, help_text='Record the result of this race. Will be automatically turned off if a custom goal is set.')),
                ('recorded', models.BooleanField(default=False)),
                ('start_delay', models.DurationField(default=datetime.timedelta(seconds=10), help_text='How long to wait before beginning the race after everyone is ready.', validators=[django.core.validators.MinValueValidator(datetime.timedelta(seconds=10)), django.core.validators.MaxValueValidator(datetime.timedelta(seconds=60))])),
                ('time_limit', models.DurationField(default=datetime.timedelta(days=1), help_text='The maximum time limit for any race entrant. Entrants who have not finished in this time will be disqualified.', validators=[django.core.validators.MinValueValidator(datetime.timedelta(seconds=3600)), django.core.validators.MaxValueValidator(datetime.timedelta(days=1))])),
                ('streaming_required', models.BooleanField(default=True, help_text='Override the streaming rules for this category. Only moderators can change this.')),
                ('allow_comments', models.BooleanField(default=True, help_text='Allow race entrants to add a glib remark after they finish.')),
                ('allow_midrace_chat', models.BooleanField(default=True, help_text='Allow users to chat during the race (race monitors can always use chat messages).')),
                ('bot_pid', models.PositiveSmallIntegerField(db_index=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetime.Category')),
                ('goal', models.ForeignKey(blank=True, help_text='Set a goal for this race. Required unless a custom goal is set.', null=True, on_delete=django.db.models.deletion.CASCADE, to='racetime.Goal')),
                ('monitors', models.ManyToManyField(blank=True, help_text='Set users (other than yourself) who can monitor this race (category owner and moderators can always monitor races).', related_name='_race_monitors_+', to=settings.AUTH_USER_MODEL)),
                ('opened_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opened_races', to=settings.AUTH_USER_MODEL)),
                ('recorded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=1000)),
                ('highlight', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('deleted_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetime.Race')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('requested', 'Requesting to join'), ('invited', 'Invited to join'), ('declined', 'Declined invitation'), ('joined', 'Joined')], default='joined', max_length=50)),
                ('ready', models.BooleanField(default=False, help_text='Ready to begin the race')),
                ('dnf', models.BooleanField(default=False, help_text='Did not finish the race')),
                ('dq', models.BooleanField(default=False, help_text='Entrant disqualified from the race')),
                ('finish_time', models.DurationField(null=True)),
                ('place', models.PositiveSmallIntegerField(null=True)),
                ('comment', models.TextField(help_text='Post-race pithy comeback from the entrant', max_length=200, null=True)),
                ('stream_live', models.BooleanField(default=False)),
                ('stream_override', models.BooleanField(default=False)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetime.Race')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The full name of this category, e.g. "Super Mario 64".', max_length=255, unique=True)),
                ('short_name', models.CharField(help_text='An abbreviation or other short identifier, e.g. "SM64".', max_length=16, unique=True)),
                ('slug', models.CharField(help_text='A unique identifier for this category used in the URL, e.g. "tetris-99".', max_length=255, unique=True)),
                ('goals', models.TextField(help_text='One goal per line. A category must have at least one goal.')),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('reviewed_at', models.DateTimeField(null=True)),
                ('accepted_as', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='racetime.Category')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='racetime.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='race',
            constraint=models.UniqueConstraint(fields=('category', 'slug'), name='unique_category_slug'),
        ),
        migrations.AddConstraint(
            model_name='goal',
            constraint=models.UniqueConstraint(fields=('category', 'name'), name='unique_category_name'),
        ),
        migrations.AddConstraint(
            model_name='entrant',
            constraint=models.UniqueConstraint(fields=('user', 'race'), name='unique_user_race'),
        ),
    ]