import React from 'react';

import './HeaderBar.css'

const HeaderBar = () => {
    return (
        <div className="header-bar-container">
            <div className='header-content-container'>
                <form>
                    <input
                    type='text'
                    placeholder='Search for anything'
                    />
                </form>
            </div>
        </div>
    )
};

export default HeaderBar;
