import { useState } from 'react';
import { useQuery, gql } from '@apollo/client';

import {
  Box,
  Flex,
  Input,
  Button,
  VStack,
  Text,
} from '@chakra-ui/react';

const ChatBox = () => {

  const [ message, setMessage ] = useState("");
  const [ buttonActive, setButtonActive ] = useState(false);

  const { loading, error, data } = useQuery(gql`
  {
    getMessages(receiverId: 1, senderId: 2) {
      id
      createdAt
      text
    }
  }
`)
  if (loading) return <p>Loading...</p>;

  const messages = data.getMessages

  const handleChange = (message) => {
    setMessage(message);
    setButtonActive(message.length > 0);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    setButtonActive(false);
    setMessage("");
  }

  return (
    <Flex
      direction="column"
      justify="space-between"
      h="90vh"
      p={4}
      m="0 auto"
      borderWidth={1}
      borderRadius="lg"
      boxShadow="md"
    >
      <VStack
        spacing={4}
        align="stretch"
        overflowY="auto"
        flex="1"
        p={2}
        borderWidth={1}
        borderRadius="lg"
      >
        {messages.map(message => {
          const isMine = message.senderId === 1;
          const alignSelf = isMine ? "flex-end" : "flex-start";
          const messageBgColor = isMine ? "blue.100" : "gray.200";

          return (
            <Box  key={message.id} alignSelf={alignSelf} bg={messageBgColor} py={4} px={6} borderRadius={18}>
              <Text>{message.text}</Text>
            </Box>
          )
        })}
      </VStack>
      <Flex as="form" mt={4} onSubmit={(e) => handleSubmit(e)}>
        <Input
          mr={2}
          borderRadius="lg"
          value={message}
          onChange={(e) => handleChange(e.target.value)}
        />
        <Button type="submit" colorScheme="blue" borderRadius="lg"
          isDisabled={!buttonActive}
        >
          Send</Button>
      </Flex>
    </Flex>
  );
};

export default ChatBox;
