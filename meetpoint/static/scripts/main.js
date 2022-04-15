function PreviewFile(file) {
    const contentPlace = document.querySelector('div.file__content')
    const reader = new FileReader()
    const dates = file.name.split('.')[0]
    const fileExtension = file.name.split('.')[file.name.split('.').length-1]
    
    reader.addEventListener('load', () => {
        if (fileExtension == 'xlsx' || fileExtension == 'xls')
            ParseExcel(reader.result, dates, fileExtension, contentPlace)
        else if (fileExtension == 'txt' || fileExtension == 'csv' || file.name.split('.').length == 1)
            ParseText(reader.result, dates, contentPlace)

        addImgDoc(fileExtension)
    }, false);

    if (fileExtension == 'xlsx' || fileExtension == 'xls')
        reader.readAsBinaryString(file)
    else
        reader.readAsText(file)
}


function ParseExcel(fileContent, dates, fileExtension, contentPlace) {
    if (document.querySelector('table.table') !== null)
        removeChilds(contentPlace)

    const workbook = null
    
    if (fileExtension === 'xlsx') {
        workbook = XLSX.read(fileContent, {type: 'binary'})
        console.log(1)
    } else if (fileExtension == 'xls') {
        const cfb = XLS.CFB.read(data, {type: 'binary'})
        workbook = XLS.parse_xlscfb(cfb)
        console.log(2)
    }

    const sheet = workbook.SheetNames[0]
    const excelRows = XLS.utils.sheet_to_row_object_array(workbook.Sheets[sheet])

    renderContent(excelRows, dates, contentPlace)
}


function ParseText(fileContent, dates, contentPlace) {
    if (document.querySelector('table.table') !== null)
        removeChilds(contentPlace)

    if (fileContent.endsWith('\n'))
        fileContent = fileContent.slice(0, -1)

    fileContent = fileContent.split('\n')
    let fileRows = []

    for (let i = 0; i < fileContent.length; i++) {
        fileRows[i] = {
            Cities: fileContent[i].split(', ')[0],
            People: fileContent[i].split(', ').slice(1)
        }
    }

    renderContent(fileRows, dates, contentPlace)
}


function renderContent(contentRows, dates, contentPlace) {
    const table = document.createElement('table')
    table.classList.add('table')
    let row = table.insertRow(-1)

    for (let i = 0; i < Object.keys(contentRows[0]).length; i++) {
        let headerCell = row.insertCell(-1)
        headerCell.classList.add('table')
        headerCell.innerHTML = Object.keys(contentRows[0])[i]
        row.appendChild(headerCell)
    }

    table.appendChild(row)

    for (let i = 0; i < contentRows.length; i++) {
        row = table.insertRow(-1)
        row.classList.add('table')

        let cell = row.insertCell(-1)
        cell.classList.add('table')
        cell.innerHTML = contentRows[i].Cities
        row.appendChild(cell)

        cell = row.insertCell(-1)
        cell.classList.add('table')
    
        if (isNumber(contentRows[i].People))
            cell.innerHTML = contentRows[i].People
        else
            cell.innerHTML = contentRows[i].People.split(', ').length

        row.appendChild(cell)
        table.appendChild(row)
    }

    contentPlace.appendChild(table)

    let datesEl = document.createElement('div')
    datesEl.classList.add('dates')

    let beginningDate = document.createElement('div')
    beginningDate.classList.add('dates')
    beginningDate.innerHTML = `Meeting beginning date: ${dates.split('_')[0].replaceAll('-', '.')}`
    datesEl.appendChild(beginningDate)

    let closingDate = document.createElement('div')
    closingDate.classList.add('dates')
    closingDate.innerHTML = `Meeting closing date: ${dates.split('_')[1].replaceAll('-', '.')}`
    datesEl.appendChild(closingDate)

    contentPlace.appendChild(datesEl)
}


function addImgDoc(fileExtension) {
    const fileDrop = document.querySelector('div.file__drop')

    if (document.querySelector('img.img__document') !== null)
        fileDrop.removeChild(document.querySelector('img.img__document'))

    let imgDoc = document.createElement('img')
    imgDoc.classList.add('img__document')
    
    if (fileExtension === 'xlsx' || fileExtension == 'xls' || fileExtension == 'csv' || fileExtension == 'txt')
        imgDoc.setAttribute('src', `/static/images/${fileExtension}.svg`)
    else
        imgDoc.setAttribute('src', `/static/images/document.svg`)

    fileDrop.appendChild(imgDoc)
}


function isNumber(value) {
    return /^-?[\d.]+(?:e-?\d+)?$/.test(value)
}


function removeChilds(parent) {
    while (parent.lastChild)
        parent.removeChild(parent.lastChild);
}
