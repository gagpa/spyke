from app import db


@db.auto_close_session
def get_containers_to_scan():
    """Получить модели контейнеров для сканирования"""
    return db.Session().query(db.Container).filter_by(is_active=True).all()


@db.auto_close_session
def get_prev_status_container(label: str):
    return db.Session().query(db.Container).filter_by(label=label).one().curr_status


@db.auto_close_session
def change_status(model, scan_data):
    model = db.Session().merge(model)
    model.curr_status = scan_data['status']
    db.Session().add(model)
    db.Session().commit()
