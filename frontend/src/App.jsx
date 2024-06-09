import { Box, Center, ChakraProvider, Square, Text } from '@chakra-ui/react'

import { extendTheme, Flex } from '@chakra-ui/react'

import SideBar from './components/SideBar'
import Main from './components/Main'

import "./style.css"

const theme = extendTheme({
  fonts: {
    body: `'Noto Sans JP', sans-serif`,
  },
})

function App() {
  return <ChakraProvider theme={theme}>
    <Flex>
      <SideBar flex="1" />
      <Main flex="1" />
    </Flex>

  </ChakraProvider>
}

export default App
