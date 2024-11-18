import logging

from app.models import db

from flask import jsonify

# IntegrityError：违反数据库约束（例如唯一性、非空等）
# DataError：数据格式或长度不符合要求，
# OperationalError：一般由于数据库连接问题（网络中断、数据库未启动等）
# ProgrammingError：通常是由于 SQL 语句有误，或是数据库表或字段不存在
from sqlalchemy.exc import IntegrityError, DataError, OperationalError, ProgrammingError

from werkzeug.exceptions import NotFound, Unauthorized, Forbidden, BadRequest

logging.basicConfig(filename='error.log', level=logging.ERROR)

def register_error_handlers(app):
# SQLAlchemy 异常处理
  @app.errorhandler(IntegrityError)
  def handle_integrity_error(e):
      db.session.rollback()
      logging.error(f"IntegrityError: {str(e)}")
      return jsonify({"message": "Integrity error: Duplicate entry or constraint violation","success": False}), 400

  @app.errorhandler(DataError)
  def handle_data_error(e):
      db.session.rollback()
      logging.error(f"DataError: {str(e)}")
      return jsonify({"error": "Data error: Invalid data format or length"}), 400

  @app.errorhandler(OperationalError)
  def handle_operational_error(e):
      logging.error(f"OperationalError: {str(e)}")
      return jsonify({"error": "Database connection error, please try again later."}), 500

  @app.errorhandler(ProgrammingError)
  def handle_programming_error(e):
      db.session.rollback()
      logging.error(f"ProgrammingError: {str(e)}")
      return jsonify({"error": "Internal server error occurred."}), 500




  # HTTP 异常处理
  @app.errorhandler(NotFound)
  def handle_not_found(e):
      logging.error(f"NotFound: {str(e)}")
      return jsonify({"error": "The requested resource was not found."}), 404

  @app.errorhandler(Unauthorized)
  def handle_unauthorized(e):
      logging.error(f"Unauthorized: {str(e)}")
      return jsonify({"error": "Unauthorized access, please log in."}), 401

  @app.errorhandler(Forbidden)
  def handle_forbidden(e):
      logging.error(f"Forbidden: {str(e)}")
      return jsonify({"error": "Access forbidden, you do not have permission."}), 403

  @app.errorhandler(BadRequest)
  def handle_bad_request(e):
      logging.error(f"BadRequest: {str(e)}")
      return jsonify({"error": "Bad request, please check your input."}), 400




  # 常见 Python 内置异常处理
  @app.errorhandler(ValueError)
  def handle_value_error(e):
      logging.error(f"ValueError: {str(e)}")
      return jsonify({"error": "Value error: Please check your input format."}), 400

  @app.errorhandler(KeyError)
  def handle_key_error(e):
      logging.error(f"KeyError: {str(e)}")
      return jsonify({"error": "Key error: Required data is missing."}), 400

  @app.errorhandler(TypeError)
  def handle_type_error(e):
      logging.error(f"TypeError: {str(e)}")
      return jsonify({"error": "Type error: Please check your input type."}), 400

  @app.errorhandler(AttributeError)
  def handle_attribute_error(e):
      logging.error(f"AttributeError: {str(e)}")
      return jsonify({"error": "Attribute error: Something went wrong with the data."}), 500

  # 捕获所有未处理的异常
  @app.errorhandler(Exception)
  def handle_unexpected_error(e):
      db.session.rollback()
      logging.error(f"UnexpectedError: {str(e)}")
      return jsonify({"error": "An unexpected error occurred, please try again later."}), 500