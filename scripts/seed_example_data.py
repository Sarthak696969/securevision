# Seeds DB with demo rows (datasets, models) for quick play.
import os, json
from securevision.db.session import SessionLocal, init_engine
from securevision.db.models import Dataset, ModelDef
from securevision.config import Settings

def main():
    settings = Settings()
    init_engine(settings.DATABASE_URL)
    db = SessionLocal()
    ds = Dataset(name="gtsrb", version="1.0", type="gtsrb", storage_uri="s3://securevision/gtsrb", checksum="")
    db.add(ds)
    md = ModelDef(name="resnet18_gtsrb", arch="resnet18", task="gtsrb", params_json="{}")
    db.add(md)
    db.commit()
    print("Seeded.")

if __name__=="__main__":
    main()
