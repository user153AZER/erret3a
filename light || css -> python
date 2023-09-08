import cssutils

css_code = """
:root {
    --border-color: #482896;
    --shadow-color: #734bd4;
    --main-bg-color: #8357eb;
    --secondary-bg-color: #986ef1;
    --lamp-light-color: #c791e5;
    --lamp-dark-color: #f679d2;
    --rope-color: #9938b8;
    --icon-color: #ebe4f1;

    --lamp-width: 140px;
    --lamp-height: 100px;
    --lamp-top-height: 20px;
}

body {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    background-color: var(--main-bg-color);
    overflow: hidden;
    width: 100vw;
    height: 100vh;
}

form {
    margin: 0;
    width: 200px;
    padding: 2em 2.2em;
    border-radius: 4px;
    background: var(--secondary-bg-color);
    box-shadow: 0 5px 15px var(--shadow-color);
}

.lamp-wrapper {
    position: relative;
    width: 100%;
    justify-content: center;
    display: flex;
}

.lamp {
    height: var(--lamp-height);
    width: var(--lamp-width);
    position: relative;
    z-index: 2;
}

.lamp-part {
    background-color: var(--lamp-dark-color);
    transform: skewX(-5deg);
    height: var(--lamp-height);
    width: 60%;
    position: absolute;
    top: 0;
    left: 0;
}
.lamp-part.-body.right {
    transform: skewX(5deg);
    left: auto;
    right: 0;
}
.lamp-part.-top {
    background: transparent;
    position: absolute;
    width: calc(var(--lamp-width) - 10px);
    height: var(--lamp-top-height);
    left: 6px;
    top: -17px;
}
.lamp-part.-top-part {
    width: 50%;
    height: var(--lamp-top-height);
    left: 0;
    top: 0;
    transform: skewX(-5deg);
    border-radius: 80% 0 0 0;
    border-top: 2px solid var(--border-color);
    border-bottom: none;
}
.lamp-part.-top-part.right {
    transform: skewX(5deg);
    left: auto;
    right: 1px;
    border-radius: 0 80% 0 0;
}
.lamp-part.-bottom {
    background: linear-gradient(#FFFFFA, #FDFFB2);
    height: calc(var(--lamp-top-height) + 10px);
    width: calc(var(--lamp-width) + 10px);
    position: absolute;
    top: auto;
    bottom: -18px;
    left: -5px;
    border-radius: 50%;
    border-top: 3px solid var(--border-color);
    border-bottom: 2px solid var(--lamp-light-color);
}
.lamp-part.-bottom:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    background: linear-gradient(var(--border-color), var(--lamp-light-color));
    border-radius: 50%;
    width: 100%;
    height: 100%;
    opacity: 1;
}
.blub {
    position: absolute;
    width: calc(var(--lamp-width) - 20px);
    height: calc(var(--lamp-height) - 20px);
    top: calc(var(--lamp-top-height) - 10px);
    left: calc(var(--lamp-top-height) - 10px);
    border-radius: 5% 3% 38% 40%;
    background-color: #FFFFFA;
    -webkit-filter: blur(15px);
    filter: blur(15px);
    z-index: 2;
    opacity: 0;
    transition: all 300ms;
}
.lamp-rope {
    position: absolute;
    width: 8px;
    height: 1200px;
    background: linear-gradient(var(--border-color) 90%, var(--rope-color));
    bottom: 100%;
    margin: auto;
}

.wall-light-shadow {
    background: linear-gradient(var(--lamp-light-color), var(--main-bg-color) 30%);
    width: 80%;
