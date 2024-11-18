from flask import  Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from .models import db


from app.core.errorHandler import register_error_handlers


# 数据库迁移
migrate =  Migrate()

def create_app():

  app = Flask(__name__)

  app.config.from_object('config.DevelopmentConfig')

  # 链接mysql数据库
  db.init_app(app)

  migrate.init_app(app, db)


  # 注册异常处理器
  register_error_handlers(app)


  # 确保在应用上下文中调用 创建表
  with app.app_context():
      db.create_all()

  
  from .routes import blueprints
  # 注册所有蓝图
  for bp in blueprints:
    app.register_blueprint(bp, url_prefix=f'/{bp.name}')

  return app

