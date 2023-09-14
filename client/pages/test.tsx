import React, { useEffect, useState } from "react"; 
import Link from 'next/link'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

function Test() {
    return (
        <><h1>Look, I made a new page!! WOOHOO!</h1>

        <ul>
            <li>
                <Link href="/">Back to Home Page</Link>
            </li>
        </ul></>
    
    )
  }
   
  export default Test