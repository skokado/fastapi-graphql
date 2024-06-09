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
      <Box w="20%" maxWidth="150px" h="97vh" mt="3vh" ml={6}>
        <SideBar flex="1" />
      </Box>
      <Box w="80%" h="97vh" mt="3vh" ml={10}>
        <Main flex="1" />
      </Box>
    </Flex>

  </ChakraProvider>
}

export default App
