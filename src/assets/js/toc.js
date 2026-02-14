
document.addEventListener('DOMContentLoaded', function () {
    const tocContainer = document.getElementById('TableOfContents');
    if (!tocContainer) return;

    const content = document.querySelector('.bd-content');
    if (!content) return;

    const headers = content.querySelectorAll('h2, h3');
    if (headers.length === 0) return;

    const ul = document.createElement('ul');
    let currentLvl = 2;
    let currentUl = ul;
    let stack = [ul];

    headers.forEach((header, index) => {
        // Ensure header has an ID
        if (!header.id) {
            header.id = 'header-' + index;
        }

        const tagLevel = parseInt(header.tagName.substring(1));
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + header.id;
        a.textContent = header.textContent;
        li.appendChild(a);

        if (tagLevel > currentLvl) {
            const newUl = document.createElement('ul');
            const lastLi = currentUl.lastElementChild;
            if (lastLi) {
                lastLi.appendChild(newUl);
                stack.push(newUl);
                currentUl = newUl;
                currentUl.appendChild(li);
            } else {
                // Handle case where h3 comes before any h2 or immediate nesting
                currentUl.appendChild(li); // Fallback
            }
        } else if (tagLevel < currentLvl) {
            while (stack.length > 1 && tagLevel < currentLvl) {
                stack.pop();
                currentUl = stack[stack.length - 1];
                currentLvl--;
            }
            currentUl.appendChild(li);
        } else {
            currentUl.appendChild(li);
        }

        // Update current level for next iteration, but clamped to logic of stack
        // Actually, logic above handles stack traversal. Standardize currentLvl to tagLevel?
        // Simpler approach:
        // Just append to current list or create new nested one.
        // Re-implementing simplified logic:
    });

    // Reset and use simpler flat structure with nesting logic if complex, 
    // or just use a robust nested builder.
    // Let's use a simpler logic for 2 levels (h2, h3).

    const rootUl = document.createElement('ul');
    let output = '';

    headers.forEach((header, index) => {
        if (!header.id) header.id = 'toc-header-' + index;

        if (header.tagName === 'H2') {
            output += `<li><a href="#${header.id}">${header.textContent}</a>`;
        } else if (header.tagName === 'H3') {
            // Check if previous was H2, if not, we might need to handle, but mostly H3 follows H2
            // Simplest HTML string manipulation for 2 levels
            if (output.endsWith('</li>')) {
                // Remove closing tag to nest
                output = output.substring(0, output.length - 5);
                output += `<ul><li><a href="#${header.id}">${header.textContent}</a></li></ul></li>`;
            } else {
                // If H3 follows H3 or starts? 
                // Let's go properly with DOM.
            }
        }
    });

    // RE-WRITE DOM LOGIC TO BE ROBUST

    const tocList = document.createElement('ul');
    let lastLi = null;
    let subUl = null;

    headers.forEach((header, index) => {
        if (!header.id) header.id = 'toc-header-' + index;

        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + header.id;
        a.textContent = header.textContent;
        li.appendChild(a);

        if (header.tagName === 'H2') {
            tocList.appendChild(li);
            lastLi = li;
            subUl = null; // Reset sub-list
        } else if (header.tagName === 'H3') {
            if (!lastLi) {
                // Edge case: H3 before any H2
                tocList.appendChild(li);
                lastLi = li;
            } else {
                if (!subUl) {
                    subUl = document.createElement('ul');
                    lastLi.appendChild(subUl);
                }
                subUl.appendChild(li);
            }
        }
    });

    tocContainer.innerHTML = '';
    tocContainer.appendChild(tocList);
});
