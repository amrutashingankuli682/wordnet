document.getElementById('wordForm').addEventListener('submit', function(event) {
  event.preventDefault();
  const word = document.getElementById('wordInput').value;
  
  fetch(`/synonyms_antonyms?word=${word}`)
      .then(response => response.json())
      .then(data => {
          const synonymsList = document.getElementById('synonymsList');
          const antonymsList = document.getElementById('antonymsList');
          synonymsList.innerHTML = '';
          antonymsList.innerHTML = '';

          data.synonyms.forEach(synonym => {
              const li = document.createElement('li');
              li.textContent = synonym;
              synonymsList.appendChild(li);
          });

          data.antonyms.forEach(antonym => {
              const li = document.createElement('li');
              li.textContent = antonym;
              antonymsList.appendChild(li);
          });

          document.getElementById('results').style.display = 'flex';
      })
      .catch(error => {
          console.error('Error fetching data:', error);
      });
});
