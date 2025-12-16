var convert = function(s, numRows) {
    if (numRows === 1 || s.length <= numRows) return s;

    const rows = new Array(numRows).fill("");
    let curRow = 0;
    let goingDown = false;

    for (let char of s) {
        rows[curRow] += char;

        // Change direction at top or bottom row
        if (curRow === 0 || curRow === numRows - 1) {
            goingDown = !goingDown;
        }

        // Move up or down
        curRow += goingDown ? 1 : -1;
    }

    return rows.join("");
};

console.log(convert("PAYPALISHIRING",3))