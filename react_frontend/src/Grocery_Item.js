import React from 'react'

export default function Grocery_Item({ grocery_item, deleteGroceryItem }) {
    
    function handleGroceryItemDelete(){
        deleteGroceryItem(grocery_item.id)
    }

    return(
        
        <div className='item-display'>
            &#8226; {grocery_item.item_name}
            <button class="delete-item" onClick={handleGroceryItemDelete}>&#10006;</button>
        </div>

    )


}