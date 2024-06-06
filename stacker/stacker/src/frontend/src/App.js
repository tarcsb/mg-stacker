import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { NotificationProvider } from './context/NotificationContext';
import Stepper from './components/Stepper';
import NotificationSettings from './components/NotificationSettings';
import SecuritySettings from './components/SecuritySettings';
import HomePage from './pages/HomePage';
import Dashboard from './pages/Dashboard';
import useShortKeys from './hooks/useShortKeys';

function App() {
  const shortKeys = {
    'Ctrl+N': () => alert('New notification shortcut!'),
    'Ctrl+D': () => alert('Dashboard shortcut!'),
  };

  useShortKeys(shortKeys);

  return (
    <NotificationProvider>
      <Router>
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/dashboard" component={Dashboard} />
        </Switch>
        <Stepper />
        <NotificationSettings />
        <SecuritySettings />
      </Router>
    </NotificationProvider>
  );
}

export default App;
