from flask import Blueprint
from flask import request, jsonify
role = Blueprint('role', __name__)

from app.models import db, Role


# 新增
@role.route('/add', methods=['POST'])
def add():
    data = request.get_json()

    newRole = Role(role_name=data['roleName'])


    db.session.add(newRole)

    db.session.commit()

    return  jsonify({'message': 'Role added successfully!'}), 200

# 更新
@role.route('/update', methods=['POST'])
def update():
    data = request.get_json()

    user = db.get_or_404(Role,data['id'] )

    user.role_name = data['roleName']

    db.session.commit()

    return  jsonify({'message': 'Role update successfully!'}), 200

# 删除
@role.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('id')

    cur = db.get_or_404(Role,id )

    db.session.delete(cur)

    db.session.commit()

    return  jsonify({'message': 'Role deleted successfully!'}), 200


# 详情
@role.route('/getOne',  methods=['GET'])
def getOne():
    id = request.args.get('id')

    detail = db.get_or_404(Role,id)

    return  jsonify(detail.to_dict()), 200

# 所有数据
@role.route('/all',  methods=['POST'])
def getAll():
    
    data = request.get_json()

    role_name = data.get('roleName')


    # 开始查询
    query = Role.query
    
    # 根据条件动态添加过滤
    if role_name:
        query = query.filter(Role.role_name.like(f"%{role_name}%"))

    roles = query.all()

        
    list= [role.to_dict() for role in roles]
    
    return  jsonify(list), 200