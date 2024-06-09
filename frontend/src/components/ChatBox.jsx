import { useState } from 'react';
import { gql, useQuery, useSubscription } from '@apollo/client';

import {
  Box,
  Flex,
  Input,
  Button,
  VStack,
  Text,
} from '@chakra-ui/react';

const ChatBox = () => {

  const [ inputText, setInputText ] = useState("");
  const [ buttonActive, setButtonActive ] = useState(false);

  const { loading, data } = useQuery(gql`
  {
    getMessages(receiverId: 1, senderId: 2) {
      id
      senderId
      createdAt
      text
    }
  }
`)
  // sample: countSubscription
  const [ subscribedCounts, setSubscribedCounts ] = useState([])
  const onCountChange = (newCount) => {
    setSubscribedCounts([...subscribedCounts, newCount])
  }
  const countSubscription = useSubscription(gql`
    subscription {
      count
    }
  `, {
    onData: ({ data }) => onCountChange(data.data.count)
  })

  // Message subscription
  const [ subscribedMessages, setSubscribedMessages  ] = useState([])
  const onMessageSubscribe = (newMessage) => {
    if (newMessage === null) return;
    setSubscribedMessages([newMessage, ...subscribedMessages])
  }
  const messageSubscription = useSubscription(gql`
    subscription {
      subscribeDm(receiverId: 1, senderId: 2) {
        id
        senderId
        createdAt
        text
      }
    }
  `, {
    onData: ({ data }) => onMessageSubscribe(data.data.subscribeDm)
  })

  if (loading || countSubscription.loading || messageSubscription.loading) return <p>Loading...</p>;

  const handleChange = (message) => {
    setInputText(message);
    setButtonActive(message.length > 0);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    setButtonActive(false);
    setInputText("");
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
        <Text>{subscribedCounts}</Text>
        {/* Messages will be displayed after opened page */}
        {subscribedMessages.map(message => {
          const isMine = message.senderId === 1;
          const alignSelf = isMine ? "flex-end" : "flex-start";
          const messageBgColor = isMine ? "blue.100" : "gray.200";

          return (
            <Box  key={message.id} alignSelf={alignSelf} bg={messageBgColor} py={4} px={6} borderRadius={18}>
              <Text>{message.text}</Text>
            </Box>
          )
        })}

        {data.getMessages.map(message => {
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
          value={inputText}
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
