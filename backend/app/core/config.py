from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # 1. Các biến bắt buộc phải có trong .env
    DB_URL: str
    SECRET_KEY: str

    # 2. Khai báo thêm các biến mà Docker/Môi trường đang truyền vào
    # Việc khai báo này giúp bạn có thể gọi settings.postgres_server trong code
    project_name: Optional[str] = "Online Auction"
    api_v1_str: Optional[str] = "/api/v1"
    postgres_server: Optional[str] = None
    postgres_user: Optional[str] = None
    postgres_password: Optional[str] = None
    postgres_db: Optional[str] = None
    postgres_port: Optional[str] = None
    kafka_bootstrap_servers: Optional[str] = None
    redis_host: Optional[str] = None
    redis_port: Optional[str] = None

    # 3. Cấu hình Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # Cho phép bỏ qua các biến thừa trong môi trường không được khai báo ở trên
        extra="ignore", 
        # Không phân biệt chữ hoa chữ thường (DB_URL hay db_url đều được)
        case_sensitive=False 
    )

settings = Settings()