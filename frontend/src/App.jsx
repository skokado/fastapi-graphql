import { Box, ChakraProvider } from '@chakra-ui/react'

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
      <Box w="15%" maxWidth="100px" h="97vh" mt="3vh" ml={6}>
        <SideBar flex="1" />
      </Box>
      <Box w="85%" h="97vh" mt="3vh" ml={8}>
        <Main flex="1" />
      </Box>
    </Flex>

  </ChakraProvider>
}

export default App
