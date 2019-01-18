function preprocessMath(contentState){
    let count = 0
    for(let block of contentState.blocks){
        let blockText = block.text
        while(blockText.match(/\t\t/)){
            blockText = blockText.replace(/\t\t/,
                `$${contentState.entityMap[count].data.teX}$`)
            count += 1
        }
        block.text = blockText
    }
    return contentState
}

module.exports = preprocessMath;