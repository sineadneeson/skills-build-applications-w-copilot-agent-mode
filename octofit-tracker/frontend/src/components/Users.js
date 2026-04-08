import React, { useEffect, useState } from 'react';
import { Table, Card } from 'react-bootstrap';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

function Users() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    console.log('Fetching Users from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setUsers(results);
        console.log('Fetched Users:', data);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, []);
  return (
    <Card className="mb-4">
      <Card.Body>
        <Card.Title as="h2" className="mb-4">Users</Card.Title>
        <Table striped bordered hover responsive>
          <thead>
            <tr>
              <th>#</th>
              <th>Username</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, idx) => (
              <tr key={user.id || idx}>
                <td>{user.id || idx + 1}</td>
                <td>{user.username}</td>
                <td>{user.email}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Card.Body>
    </Card>
  );
}

export default Users;