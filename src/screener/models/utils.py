from pydantic import BaseModel


class Model(BaseModel):
    def save(self):
        model_json = self.model_dump_json()
        print(model_json)
