import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../../src/App';

test('renders Stepper component', () => {
  render(<App />);
  const element = screen.getByText(/Stepper Component/i);
  expect(element).toBeInTheDocument();
});

test('renders Notification Settings component', () => {
  render(<App />);
  const element = screen.getByText(/Notification Settings/i);
  expect(element).toBeInTheDocument();
});

test('renders Security Settings component', () => {
  render(<App />);
  const element = screen.getByText(/Security Settings/i);
  expect(element).toBeInTheDocument();
});
