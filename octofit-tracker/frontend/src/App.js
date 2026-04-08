
import logo from './logo.svg';
import { Container, Nav, Navbar } from 'react-bootstrap';
import { Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';

function App() {
  return (
    <>
      <Navbar expand="lg" className="navbar">
        <Container>
          <Navbar.Brand as={Link} to="/">
            <img src={logo} alt="OctoFit Logo" className="octofit-logo" />
            OctoFit Tracker
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/activities">Activities</Nav.Link>
              <Nav.Link as={Link} to="/leaderboard">Leaderboard</Nav.Link>
              <Nav.Link as={Link} to="/teams">Teams</Nav.Link>
              <Nav.Link as={Link} to="/users">Users</Nav.Link>
              <Nav.Link as={Link} to="/workouts">Workouts</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Container className="mt-4">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<div className="text-center"><h1 className="display-4 mb-4">Welcome to OctoFit Tracker!</h1><p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p></div>} />
        </Routes>
      </Container>
    </>
  );
}

export default App;
