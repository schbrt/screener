from pydantic import BaseModel
import pyarrow as pa
import pyarrow.parquet as pq


class Model(BaseModel):
    def save(self):
        class_name = self.__class__.__name__.lower()
        dest = f"./parquet/{class_name}.parquet"

        model_dict = self.model_dump()
        table = pa.Table.from_pydict(model_dict)
        pq.write_table(table, dest)
