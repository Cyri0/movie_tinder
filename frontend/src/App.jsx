import React, {useState, useEffect} from 'react'


const App = () => {
  const [movies, setMovies] = useState([])
  const [movieIndex, setMovieIndex] = useState(0)

  useEffect(()=>{
    fetch('http://127.0.0.1:8000/api/movies/')
    .then(res => res.json())
    .then(apiMovies => {
      setMovies(apiMovies)
      console.log(apiMovies);
    })
  }, [])

  return (
    <div>

      {movies.length > 0?
      <div className='card'>
        <h2>{ movies[movieIndex].title }</h2>
      </div>:
      <div>Loading...</div>
      }

      <div className='buttons'>
        <button>💩</button>
        <button>😎</button>
      </div>
    </div>
  )
}

export default App