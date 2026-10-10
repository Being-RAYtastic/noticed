const input = document.getElementById("photo")
const inputSlot = document.getElementById("today")

if (input) {
    input.addEventListener("change", () => {
        if (!input.files.length) return

        inputSlot.classList.add("busy")
        input.form.submit()
        setTimeout(() => { input.disabled = true }, 0)
    })

    window.addEventListener("pageshow", () => {
        input.disabled = false
        inputSlot.classList.remove("busy")
    })
}

