import React from 'react';


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
