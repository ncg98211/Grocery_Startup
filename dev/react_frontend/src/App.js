import './App.css';
import Grocery_List from './Grocery_List'
import {React, useState, useRef, useEffect} from 'react'
import { v4 as uuidv4 } from 'uuid';
import react_logo from './react.png'
import flask_logo from './flask.png'
import heart from './heart.png'
import grocery_cart from './grocery_cart.png'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

function App() {
  const [grocery_items, setGroceryItems] = useState([])
  const groceryItemRef = useRef()


  useEffect(() => {
      fetch('http://127.0.0.1:5000/api/grocery_items/1')
      .then(res => {
        if (!res.ok) { // error coming back from server
          throw Error('could not fetch the data for that resource');
        } 
        return res.json();
      })
      .then(data => {
        setGroceryItems(data[1])
      })
      .catch(err => {
        // auto catches network / connection error
        setGroceryItems([])
      })
  }, [])


  function deleteGroceryItem(id){
    const newGroceryItems = [...grocery_items]
    const filteredGroceryItems = newGroceryItems.filter(item => item.id !== id)
    
    fetch('http://127.0.0.1:5000/api/grocery_items/delete/' + id)  
    setGroceryItems(filteredGroceryItems)
  }

  function handleAddItem(e){
    const groceryItemName = groceryItemRef.current.value
    const newItemId = uuidv4()
    if (groceryItemName === '') return 
      setGroceryItems(previousItems => {
        return [...previousItems,{id: newItemId, item_name: groceryItemName}]

      })
      fetch('http://127.0.0.1:5000/api/grocery_items/1', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          mode: 'cors',
          body: JSON.stringify({
            item_name: groceryItemName,
            grocery_list_id: 1,
            item_id: newItemId
          })
        })
    groceryItemRef.current.value = null
  }

  
  return (
    <>
      <div className='app-background'>
			<div className='main-container'>

      <div className='title'>Grocery List
      <img src={grocery_cart}></img>
      </div>

      <Grocery_List deleteGroceryItem={deleteGroceryItem} grocery_items={grocery_items} />
      <div className='add-item-box'><input ref={groceryItemRef} type="text" className='add-item-input' placeholder='Add a grocery item...'/>
      <FontAwesomeIcon icon={faPlus} onClick={() => handleAddItem()} />
      </div>
      <div className='item-count'>
      <b>{grocery_items.length}</b> item(s) in List
      </div>
      <div className='made-with'>
        Made With:
      <div className='react-logo'>
        <img src={react_logo}></img>
      </div>

      <div className='flask-logo'>
        <img src={flask_logo}></img>
      </div>

      <div className='heart'>
        <img src={heart}></img>
      </div>

      </div>

      </div>
      </div>
    </>
  )
}

export default App;
