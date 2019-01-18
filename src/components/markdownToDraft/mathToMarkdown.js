function preprocessMath(contentState){
    let count = 0
    for(let block of contentState.blocks){
        let blockText = block.text
        while(blockText.match(/\t\t/)){
            for(let i = count; i <Object.keys(contentState.entityMap).length;i++){
                if(contentState.entityMap[i].type === "INLINETEX"){
                    count = i
                    break
                }
            }
            let formula = contentState.entityMap[count].data.teX
            blockText = blockText.replace(/\t\t/,"$"+formula+"$")
            count += 1
        }
        block.text = blockText
    }
    return contentState
}

module.exports = preprocessMath;