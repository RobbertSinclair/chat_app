import React, {Component} from "react";
import { render } from "react-dom";
import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../../node_modules/bootstrap/dist/js/bootstrap.min.js";


export default class App extends Component {
    
    render() {
        return (
            <div>
                <h1>Hello World</h1>
            </div>
            );
    }
}

const appDiv = document.getElementById("root");
render(<App />, appDiv);