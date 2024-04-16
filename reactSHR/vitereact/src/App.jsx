import React, { useState } from 'react'

function App() {
  let [a,b]=useState(69);
  return (
    <div className='text-white w-full h-screen bg-zinc-800'>
      <h1>{a}</h1>
    </div>
  )
}

export default App