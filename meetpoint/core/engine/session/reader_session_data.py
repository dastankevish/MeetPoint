def get_session_data(id):
    with open(f'sessions/{id}') as session_data:
        return session_data.read()
