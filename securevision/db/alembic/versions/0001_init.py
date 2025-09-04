from alembic import op
import sqlalchemy as sa

revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table("datasets",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(64)),
        sa.Column("version", sa.String(32)),
        sa.Column("type", sa.String(32)),
        sa.Column("storage_uri", sa.Text),
        sa.Column("checksum", sa.String(128)),
        sa.Column("created_at", sa.DateTime),
    )
    op.create_table("modeldefs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(64)),
        sa.Column("arch", sa.String(32)),
        sa.Column("task", sa.String(32)),
        sa.Column("params_json", sa.Text),
        sa.Column("created_at", sa.DateTime),
    )
    op.create_table("experiments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(128)),
        sa.Column("task", sa.String(32)),
        sa.Column("dataset_id", sa.Integer),
        sa.Column("modeldef_id", sa.Integer),
        sa.Column("config_yaml", sa.Text),
        sa.Column("status", sa.String(32)),
        sa.Column("created_at", sa.DateTime),
        sa.Column("started_at", sa.DateTime, nullable=True),
        sa.Column("finished_at", sa.DateTime, nullable=True),
    )
    op.create_table("artifacts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("experiment_id", sa.Integer),
        sa.Column("kind", sa.String(32)),
        sa.Column("path", sa.Text),
        sa.Column("size_bytes", sa.Integer),
        sa.Column("checksum", sa.String(128)),
        sa.Column("created_at", sa.DateTime),
    )
    op.create_table("metrics",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("experiment_id", sa.Integer),
        sa.Column("key", sa.String(64)),
        sa.Column("value_float", sa.Float),
        sa.Column("context_json", sa.Text),
        sa.Column("created_at", sa.DateTime),
    )
    op.create_table("jobs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("celery_id", sa.String(64)),
        sa.Column("type", sa.String(32)),
        sa.Column("status", sa.String(32)),
        sa.Column("request_json", sa.Text),
        sa.Column("result_json", sa.Text),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
    )
    op.create_table("federated_runs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("base_experiment_id", sa.Integer),
        sa.Column("num_clients", sa.Integer),
        sa.Column("malicious_frac", sa.Float),
        sa.Column("aggregator", sa.String(32)),
        sa.Column("status", sa.String(32)),
        sa.Column("created_at", sa.DateTime),
    )

def downgrade() -> None:
    for t in ["federated_runs","jobs","metrics","artifacts","experiments","modeldefs","datasets"]:
        op.drop_table(t)
