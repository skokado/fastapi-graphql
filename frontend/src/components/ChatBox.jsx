import { useState } from 'react';

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

  const handleChange = (message) => {
    setMessage(message);
    setButtonActive(message.length > 0);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(message)
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
        {/* Dummy Messages */}
        <Box alignSelf="flex-start" bg="gray.200" py={4} px={6} borderRadius={18}>
          <Text>Hello!</Text>
        </Box>
        <Box alignSelf="flex-end" bg="blue.100" py={4} px={6} borderRadius={18}>
          <Text>Hi there!</Text>
        </Box>
        {/* Add more messages here */}
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
