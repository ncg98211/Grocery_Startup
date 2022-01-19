import React from 'react'
import Grocery_Item from './Grocery_Item'


export default function Grocery_List({ grocery_items, deleteGroceryItem }){
    return (
    grocery_items.map(grocery_item => {
        return <Grocery_Item key={grocery_item.id} deleteGroceryItem={deleteGroceryItem} grocery_item={grocery_item} />
    }) 
  )
}