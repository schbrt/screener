from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Screener"
    POLYGON_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
