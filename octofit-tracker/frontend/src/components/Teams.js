import React, { useEffect, useState } from 'react';
import { Table, Card } from 'react-bootstrap';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

function Teams() {
  const [teams, setTeams] = useState([]);
  useEffect(() => {
    console.log('Fetching Teams from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setTeams(results);
        console.log('Fetched Teams:', data);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, []);
  return (
    <Card className="mb-4">
      <Card.Body>
        <Card.Title as="h2" className="mb-4">Teams</Card.Title>
        <Table striped bordered hover responsive>
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, idx) => (
              <tr key={team.id || idx}>
                <td>{team.id || idx + 1}</td>
                <td>{team.name}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Card.Body>
    </Card>
  );
}

export default Teams;