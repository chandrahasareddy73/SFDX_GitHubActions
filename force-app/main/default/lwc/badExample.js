// badExample.js
import { LightningElement, track } from 'lwc';

export default class BadExample extends LightningElement {
    // ❌ Using @track unnecessarily for primitive values
    @track counter = 0;

    // ❌ Direct DOM manipulation (not recommended in LWC)
    renderedCallback() {
        this.template.querySelector('div').innerHTML = 'Changed directly!';
    }

    // ❌ No input validation
    handleInputChange(event) {
        this.counter = event.target.value; // Could be non-numeric
    }
}
