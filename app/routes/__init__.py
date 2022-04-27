from flask import Flask

def init_app(app: Flask):
    from .user_blueprint import bp_users
    from .categories_blueprint import bp_categories
    from .homepage_blueprint import bp_homepage
    from .tasks_blueprint import bp_tasks

    app.register_blueprint(bp_users)
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_homepage)
    app.register_blueprint(bp_tasks)