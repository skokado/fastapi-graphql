import { Avatar, Box, Divider, Flex, Grid, GridItem, SimpleGrid, Text, useRadio } from "@chakra-ui/react"

import ChatBox from "./ChatBox"

const Main = () => {

  const users = [
    {
      id: 1,
      username: "Alice"
    },
    {
      id: 2,
      username: "Bob"
    },
    {
      id: 4,
      username: "Chris"
    },
  ]

  return (
    <div>
      <Flex>
        {/* User List Box */}
        <Box
          flex="1"
          borderWidth="1px" borderRadius={8}
          p={4}
          maxWidth="40%"
          maxHeight={400}
        >
          <Box mb={4}>
            <Text fontSize="2xl" as="b">Groups</Text>
          </Box>

          <SimpleGrid columns={1} spacing={2}>
            {users.map(( user, id ) => {
              return user.username !== "Bob" && <div key={user.id}>
                <Grid templateColumns="repeat(10, 1fr)" gap={2} mb={2}>
                  <GridItem colStar={1} h="100%">
                    <Avatar size="sm" name={user.username} />
                  </GridItem>
                  <GridItem colStart={3}>
                    <Text fontSize="md">{user.username}</Text>
                  </GridItem>
                  <GridItem colStart={7}>
                    {/* <Text fontSize="md">Foo</Text> */}
                  </GridItem>
                </Grid>

                { id < users.length - 1 && <Divider /> }
              </div>
            })}
          </SimpleGrid>
        </Box>

        {/* Chat Box */}
        <Box
          flex="1"
          ml={8}
        >
          <ChatBox />
        </Box>

      </Flex>
    </div>
  )
}

export default Main
