import { useEffect } from 'react';

const useShortKeys = (shortKeys) => {
  useEffect(() => {
    const handleKeyDown = (event) => {
      const key = `${event.ctrlKey ? 'Ctrl+' : ''}${event.key}`;
      if (shortKeys[key]) {
        event.preventDefault();
        shortKeys[key]();
      }
    };

    window.addEventListener('keydown', handleKeyDown);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [shortKeys]);
};

export default useShortKeys;
